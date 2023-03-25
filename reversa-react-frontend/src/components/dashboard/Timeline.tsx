import { Card, Container, Stack } from 'react-bootstrap';
import { Student } from "../../entities/Student"


export function Timeline({schedule}: Student) {
    return (
        <Container style={{ maxWidth: "720px" }}>
            <h1 className='text-center'>Upcoming</h1>
            {schedule.items.map(i =>
                <Card className="text-center" style={{ margin: 10 }}>
                    <Card.Body>
                        <Container>
                            <Stack direction="horizontal" gap={5}>
                                <div>
                                    {i.startDate.toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })}
                                </div>
                                <div>
                                    {i.room.name}
                                </div>
                                <div className='justify-content-end'>
                                    {i.room.location.name}
                                </div>
                            </Stack>
                        </Container>
                    </Card.Body>
                </Card>
            )}
        </Container>
    )
}