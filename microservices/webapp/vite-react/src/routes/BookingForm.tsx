import { useContext, useEffect, useState } from 'react'
import { Button, Card, Center, Checkbox, Container, Flex, Grid, Group, Input, SimpleGrid, Stack, Text } from '@mantine/core'
import { ResetTimeBlocks, TimeBlocks } from '../components/timeselector/TimeBlocks'
import { Form, useParams, useNavigate } from "react-router-dom";
import { DatePicker } from '@mantine/dates'
import { PopupMessage } from '../components/Utilities/PopupMessage'
import { Configuration, UnavailabilitiesPostOperationRequest, UnavailabilityApi, ItemApi  } from '../reserva_client'
import { ConfigContext } from '../contexts/ConfigProvider'
import { GetTokenSilentlyOptions, useAuth0 } from '@auth0/auth0-react'

export type TimeRange = {
    startTime?: Date;
    endTime?: Date;
};


export function BookingForm() {
    const config = useContext(ConfigContext);
    const { getAccessTokenSilently, user } = useAuth0();
    const [value, setValue] = useState<Date | null>(new Date());
    const [selectedTime, setSelectedTime] = useState<TimeRange>({});
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [isErrorPopupOpen, setIsErrorPopupOpen] = useState(false);

    const [bookingFormData, setBookingFormData] = useState<UnavailabilitiesPostOperationRequest>({});

    const { roomId } = useParams(); // This is the roomId from the URL 

    const roomName = roomId;

    useEffect(() => {
        ResetTimeBlocks();
    }, [value]);

    const navigate = useNavigate();
    const handleFormCancelAction = () => {
        navigate('/');
    }

    const handleTimeBlockChange = (timeRange: TimeRange) => {
        setSelectedTime(timeRange);
        if (timeRange.startTime !== undefined) {
            setIsPopupOpen(true);
            setIsErrorPopupOpen(false);
        }
        else {
            setIsPopupOpen(false);
        }
    };

    const handlePopupClose = () => {
        setSelectedTime({});
        setIsPopupOpen(false);
        setIsErrorPopupOpen(false);
        ResetTimeBlocks();
    };

    function GetDate() {
        if(value !== null){
            //console.log(value);
            return value;//.toLocaleString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
        }
        else
            return new Date();
    }

    function GetStartTime() {
        var startTime:Date = new Date();
        if(GetDate()){
            startTime = GetDate();
        }
        if(selectedTime.startTime){
            startTime.setHours(selectedTime.startTime.getHours());
            startTime.setMinutes(selectedTime.startTime.getMinutes());
            startTime.setSeconds(selectedTime.startTime.getSeconds());
            startTime.setMilliseconds(selectedTime.startTime.getMilliseconds());
        }
        return startTime;//.toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true });
    }

    function GetEndTime() {
        var endTime:Date = new Date();
        if(GetDate()){
            endTime = GetDate();
        }
        if(selectedTime.endTime){
            endTime.setHours(selectedTime.endTime.getHours());
            endTime.setMinutes(selectedTime.endTime.getMinutes() + 29);
            endTime.setSeconds(selectedTime.endTime.getSeconds());
            endTime.setMilliseconds(selectedTime.endTime.getMilliseconds());
        }
        return endTime;//.toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true });
    }



    function ConstructMessage() {
        const startTimeText = GetStartTime().toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true });
        const endTimeText = GetEndTime().toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true });
        const dateTimeText = GetDate().toLocaleString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
        return "You've selected " + startTimeText + (selectedTime.endTime ? " - " + endTimeText : "") + " on " + dateTimeText;
    }

    function ConstructErrorMessage() {
        return "Please select a time.";
    }

    const handleBookingSubmit = () => {
        if (selectedTime.startTime !== undefined){
            var accessTokenOptions = {
                authorizationParams: {
                    audience: config?.api.baseUrl,
                }
            } as GetTokenSilentlyOptions;
    
            const unavailabilityApi = new UnavailabilityApi(
                new Configuration({ basePath: config?.api.baseUrl, accessToken: "Bearer " + getAccessTokenSilently(accessTokenOptions) })
            );
    
            unavailabilityApi.unavailabilitiesPost({
                unavailabilitiesPostRequest: {
                    item: (roomId) ? roomId : "",
                    startDate: GetStartTime().toISOString(),
                    endDate: GetEndTime().toISOString(),
                    owner: user?.sub,
                    type: "booking"
                }
            }).then((response) => {
                console.log(response);
                navigate('/bookings');
            }
            ).catch((error) => {
                console.log(error);
            });
        }
        else {
            setIsErrorPopupOpen(true);
        }
    }

    function GetRoomUnavailability(){
        var accessTokenOptions = {
            authorizationParams: {
                audience: config?.api.baseUrl,
            }
        } as GetTokenSilentlyOptions;

        const itemApi = new ItemApi(
            new Configuration({ basePath: config?.api.baseUrl, accessToken: "Bearer " + getAccessTokenSilently(accessTokenOptions) })
        );
        
        itemApi.itemsIdUnavailabilitiesGet({
            id: (roomId) ? roomId : "",
            start: GetDate(),
            end: GetDate()
        }).then((response) => {
            console.log(response);
        }
        ).catch((error) => {
            console.log(error);
        });
    }

    return (
        <Stack align='center'>
            <Text size={24} weight={700} >Booking Form for {roomName}</Text>
            <Card w="75%" sx={{ maxWidth: 500 }}>
                <Card.Section mb={5}>
                    <Text size={18} weight="bold" align='left'>Room Summary</Text>
                </Card.Section>
                <Card.Section>
                    <Group spacing={0}>
                        <Stack w="50%" spacing={0}>
                            <Text align='left' size={14}>[Placeholder]</Text>
                            <Text align='left' size={14}>[Placeholder]</Text>
                            <Text align='left' size={14}>[Placeholder]</Text>
                            <Text align='left' size={14}>[Placeholder]</Text>
                        </Stack>
                        <Stack w="50%" spacing={0}>
                            <Text align='right' size={14}>[Placeholder]</Text>
                            <Text align='right' size={14}>[Placeholder]</Text>
                            <Text align='right' size={14}>[Placeholder]</Text>
                            <Text align='right' size={14}>[Placeholder]</Text>
                        </Stack>
                    </Group>
                </Card.Section>
            </Card>
            <Card w="75%" sx={{ maxWidth: 500 }}>
                <Card.Section mb={5}>
                    <Text size={18} weight="bold" align='left'>Booking Details</Text>
                </Card.Section>
                <Card.Section mb={5}>
                    <Text align='left' size={12}>Select Your Booking Time</Text>
                    <Group sx={{ justifyContent: 'space-between' }}>
                        <DatePicker
                            h={30 * 8}
                            value={value}
                            onChange={setValue}
                            firstDayOfWeek={0}
                            weekdayFormat="ddd"
                            minDate={new Date()}
                            maxDate={new Date(new Date().setDate(new Date().getDate() + 28 - 1))}
                            size="xs"
                            maxLevel="month"
                            hideOutsideDates={true}
                        />
                        <TimeBlocks onChange={handleTimeBlockChange} />
                    </Group>
                </Card.Section>
                {
                    isPopupOpen &&
                    <Card.Section mb={5}>
                        <PopupMessage iconType={'calendarEvent'} message={ConstructMessage()} size={'xs'} onClose={() => { handlePopupClose() }} />
                    </Card.Section>
                }
                {
                    isErrorPopupOpen &&
                    <Card.Section mb={5}>
                        <PopupMessage iconType={'error'} message={ConstructErrorMessage()} size={'xs'} onClose={() => { handlePopupClose() }} />
                    </Card.Section>
                }
                <Card.Section mb={5}>
                    <Checkbox size='xs' mb={5} label="Make this a group session" />
                    <Checkbox size='xs' mb={5} label="Make this a Study with me session" />
                </Card.Section>
                <Card.Section>
                    <Form>
                        <Group position='center'>
                            <Button type='button' size='xs' color="blue" variant="filled" onClick={handleBookingSubmit}>Submit My Booking</Button>
                            <Button type='button' size='xs' color="red" variant='filled' onClick={ handleFormCancelAction }>Cancel</Button>
                        </Group>
                    </Form>
                </Card.Section>
            </Card>
        </Stack>
    )
}