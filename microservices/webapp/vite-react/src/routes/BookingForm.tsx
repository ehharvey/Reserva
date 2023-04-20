import { useEffect, useState } from 'react'
import reactLogo from '../assets/react.svg'
import viteLogo from '/vite.svg'
import { Button, Card, Center, Checkbox, Container, Flex, Grid, Group, SimpleGrid, Stack, Text } from '@mantine/core'
import { ResetTimeBlocks, TimeBlocks } from '../components/timeselector/TimeBlocks'
import { useParams } from "react-router-dom";
import { DatePicker } from '@mantine/dates'
import { PopupMessage } from '../components/Utilities/PopupMessage'

export type TimeRange = {
    startTime?: Date;
    endTime?: Date;
};


export function BookingForm() {
    const [value, setValue] = useState<Date | null>(new Date());
    const [selectedTime, setSelectedTime] = useState<TimeRange>({});
    const [isPopupOpen, setIsPopupOpen] = useState(false);

    const { roomId } = useParams(); // This is the roomId from the URL 

    const roomName = "Room 1";

    useEffect(() => {
        ResetTimeBlocks();
      }, [value]);

    const handleTimeBlockChange = (timeRange: TimeRange) => {
        setSelectedTime(timeRange);
        if(timeRange.startTime !== undefined){
            setIsPopupOpen(true);
            console.log(timeRange.startTime);
        }
        else{
            setIsPopupOpen(false);
        }
    };

    const handlePopupClose = () => {
        setSelectedTime({});
        setIsPopupOpen(false);
        ResetTimeBlocks();
    };

    function ConstructMessage() {
        const startTime = new Date(selectedTime.startTime?.getTime() || 0);

        const endTime = new Date((selectedTime.endTime)? selectedTime.endTime?.getTime() || 0 : selectedTime.startTime?.getTime() || 0);
        endTime?.setMinutes(endTime.getMinutes() + 29);

        const dateText = value?.toLocaleString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
        const startTimeText = startTime?.toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true });
        const endTimeText = endTime?.toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true });
        
        return "You've selected " + startTimeText + (endTime ? " - " + endTimeText : "") + " on " + dateText;
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

                <Card.Section mb={5}>
                    <Checkbox size='xs' mb={5} label="Make this a group session" />
                    <Checkbox size='xs' mb={5} label="Make this a Study with me session" />
                </Card.Section>
                <Card.Section>
                    <Button color="blue" variant="filled" type='submit' size='xs'>Submit my Booking</Button>
                </Card.Section>
            </Card>
        </Stack>
    )
}