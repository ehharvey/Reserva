import { Card, Divider, Group, Stack, Text } from "@mantine/core"
import { useContext, useEffect, useState } from "react";
import { UsersMeUnavailabilitiesGetRequest, UserApi, Configuration, Unavailability, ItemApi } from '../reserva_client'
import { GetTokenSilentlyOptions, useAuth0 } from "@auth0/auth0-react";
import { ConfigContext } from "../contexts/ConfigProvider";

export function BookingList() {
    const config = useContext(ConfigContext);
    const { getAccessTokenSilently, user } = useAuth0();
    const [unavailabilities, setUnavailabilities] = useState<Unavailability[]>([]);
    const [reversedUnavailabilities, setReversedUnavailabilities] = useState<Unavailability[]>([]);

    var accessTokenOptions = {
        authorizationParams: {
            audience: config?.api.baseUrl,
        }
    } as GetTokenSilentlyOptions;

    const itemApi = new ItemApi(
        new Configuration({ basePath: config?.api.baseUrl, accessToken: "Bearer " + getAccessTokenSilently(accessTokenOptions) })
    );


    useEffect(() => {
        var accessTokenOptions = {
            authorizationParams: {
                audience: config?.api.baseUrl,
            },
        } as GetTokenSilentlyOptions;

        const unavailabilityApi = new UserApi(
            new Configuration({
                basePath: config?.api.baseUrl,
                accessToken: "Bearer " + getAccessTokenSilently(accessTokenOptions),
            })
        );

        unavailabilityApi.usersMeUnavailabilitiesGet({}).then((response) => {
            const newUnavailabilities: Unavailability[] = [];
            response.unavailabilities?.forEach((unavailability, index) => {
                console.log(index);
                newUnavailabilities.push(unavailability);
            });

            newUnavailabilities.sort((a, b) => {
                const dateA = new Date(a.startDate);
                const dateB = new Date(b.startDate);
                return dateA.getTime() - dateB.getTime();
              });

            setUnavailabilities(newUnavailabilities);
            setReversedUnavailabilities([...newUnavailabilities].reverse());
        })
        .catch((error) => {
            console.log(error);
        });
    }, []);

    const bookingCard = (unavailability: Unavailability, active: boolean) => {
        const bookingStartDate: Date = new Date(unavailability.startDate);
        const bookingEndDate: Date = new Date(unavailability.endDate);
        const currentDate: Date = new Date();
        if (active) {
            return ((currentDate < bookingEndDate) ?
                <Card withBorder mb={5}>
                    <Stack>
                        <Text size="xs" align="left">
                            {bookingStartDate.toLocaleString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
                        </Text>
                        <Text size="xs" align="left">
                            {bookingStartDate.toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true }) + " - " + bookingEndDate.toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true })}
                        </Text>
                    </Stack>
                </Card> : <></>
            )
        }
        else {
            return (
                (currentDate > bookingEndDate) ?
                    <Card withBorder mb={5}>
                        <Stack>
                            <Text size="xs" align="left">
                                {bookingStartDate.toLocaleString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
                            </Text>
                            <Text size="xs" align="left">
                                {bookingStartDate.toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true }) + " - " + bookingEndDate.toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true })}
                            </Text>
                        </Stack>
                    </Card> : <></>
            )
        }

    };

    return (
        <Stack align="center">
            <Card w="75%" sx={{ maxWidth: 1000 }}>
                <Card.Section mb={5}>
                    <Text size={18} weight="bold" align="left">
                        Active Bookings
                    </Text>
                </Card.Section>
                <Card.Section>
                    {unavailabilities.length === 0 ? (<Divider my="xs" label="No active bookings" labelPosition="center" />) :
                        (
                        unavailabilities.map((unavailability) => {
                            return bookingCard(unavailability, true);
                        })
                    )}
                </Card.Section>
            </Card>
            <Card w="75%" sx={{ maxWidth: 1000 }}>
                <Card.Section mb={5}>
                    <Text size={18} weight="bold" align="left">
                        Past Bookings
                    </Text>
                </Card.Section>
                <Card.Section mb={5}>
                    {reversedUnavailabilities.length === 0 ? (<Divider my="xs" label="No past bookings" labelPosition="center" />) :
                            (
                                <>
                                    {
                                    reversedUnavailabilities.map((unavailability) => {                                   
                                        return bookingCard(unavailability, false);
                                    })}
                                    <Divider my="xs" label="Only show up to 10 past bookings" labelPosition="center" />
                                </>
                            )}
                </Card.Section>
            </Card>
        </Stack>
    );
}
