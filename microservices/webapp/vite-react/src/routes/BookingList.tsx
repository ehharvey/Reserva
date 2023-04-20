import { Card, Divider, Group, Stack, Text } from "@mantine/core"

interface Booking {

}

const activeListStub: Booking[] = [];
const pastListStub: Booking[] = [{}, {}, {}, {}, {}];

export function BookingList() {


    const bookingCard = (booking: Booking) => {
        return (
            <Card withBorder mb={5}>

            </Card>
        )
    }

    return (
        <Stack align='center'>
            <Card w="75%" sx={{ maxWidth: 500 }}>
                <Card.Section mb={5}>
                    <Text size={18} weight="bold" align='left'>Active Bookings</Text>
                </Card.Section>
                <Card.Section>
                    {
                        (activeListStub.length == 0) ?
                            <Divider my="xs" label="No active bookings" labelPosition="center" />
                            :
                            activeListStub.map((booking) => {
                                return bookingCard(booking);
                            })
                    }
                </Card.Section>
            </Card>
            <Card w="75%" sx={{ maxWidth: 500 }}>
                <Card.Section mb={5}>
                    <Text size={18} weight="bold" align='left'>Past Bookings</Text>
                </Card.Section>
                <Card.Section mb={5}>
                    {
                        (pastListStub.length == 0) ?
                            <Divider my="xs" label="No past bookings" labelPosition="center" />
                            :
                            <>
                                {pastListStub.map((booking) => {
                                    return bookingCard(booking);
                                })}
                                <Divider my="xs" label="Only show up to 10 past bookings" labelPosition="center" />
                            </>
                    }
                </Card.Section>
            </Card>
        </Stack>
    )
}