import { Group } from "../../entities/Group";
import { Button, Card, Container, Form, ListGroup, ListGroupItem } from "react-bootstrap";
import CardHeader from "react-bootstrap/esm/CardHeader";
import { ChangeEvent, useState } from "react";



export function BookingPage({ groups }: { groups: Group[] }) {
    const [selectedGroup, setGroup] = useState<Group | null>(null);

    const handleGroupSelect = (event: ChangeEvent<HTMLSelectElement>) => {
        const selectedGroup = event.target.value;
        const group = groups.find((g) => g["id"] === parseInt(selectedGroup));
        setGroup(group || null);
    };


    console.log(selectedGroup);
    return (
        <div>
            <Container>
                <Card className="mb-4">
                    <Card.Body>
                        <Card.Title>Room Summary</Card.Title>
                        <Card.Text>
                            <ListGroup variant="flush">
                                <ListGroup.Item className="d-flex justify-content-between align-items-center border-0 px-0 pb-0">
                                    Room Name
                                    <span><strong>1B25</strong></span>
                                </ListGroup.Item>
                                <ListGroup.Item className="d-flex justify-content-between align-items-center border-0 px-0 pb-0">
                                    Location
                                    <span><strong>Conestoga College - Waterloo Campus</strong></span>
                                </ListGroup.Item>
                                <ListGroup.Item className="d-flex justify-content-between align-items-center border-0 px-0 pb-0">
                                    Room Capacity
                                    <span><strong>6</strong></span>
                                </ListGroup.Item>

                            </ListGroup>
                        </Card.Text>
                    </Card.Body>

                </Card>
                <Card className="mb-4">
                    <Card.Body>
                        <Card.Title>Booking Detail</Card.Title>
                        <Card.Text>
                            <ListGroup variant="flush">
                                <ListGroup.Item className="d-flex justify-content-between align-items-center border-0 px-0 pb-0">
                                    Date
                                    <span><strong>4/1/2023</strong></span>
                                </ListGroup.Item>
                                <ListGroup.Item className="d-flex justify-content-between align-items-center border-0 px-0 pb-0">
                                    Time
                                    <span><strong>1:00PM - 2:00PM</strong></span>
                                </ListGroup.Item>

                            </ListGroup>

                            <Form>
                                <Form.Group className="mb-3" >
                                    <Form.Text>
                                        Your password must be 8-20 characters long, contain letters and numbers,
                                        and must not contain spaces, special characters, or emoji.
                                    </Form.Text>
                                </Form.Group>

                                <Form.Group className="mb-3" >
                                    <Form.Label>Select a group:</Form.Label>
                                    <Form.Select onChange={handleGroupSelect}>
                                        <option>Open this select menu</option>
                                        {groups.map((group) => (
                                            <option key={group.id} value={group.id}>
                                                {group.name}
                                            </option>
                                        ))}
                                        <option value="new">Create new group</option>
                                    </Form.Select>
                                </Form.Group>

                                {selectedGroup && (
                                    <Form.Group controlId="memberList">
                                        <Form.Label>Members:</Form.Label>
                                        <ul>
                                            {selectedGroup.member.map((member) => (
                                                <li key={member}>{member}</li>
                                            ))}
                                        </ul>
                                    </Form.Group>
                                )}

                                <Form.Group className="mb-3" controlId="formBasicCheckbox">
                                    <Form.Check type="checkbox" label="Book as group" />
                                    <Form.Check type="checkbox" label="Study With Me" />
                                </Form.Group>

                                <Form.Group className="mb-3 d-flex justify-content-end" controlId="formSubmitButton" >
                                    <Button variant="primary" type="submit"> Submit </Button>
                                </Form.Group>


                            </Form>

                        </Card.Text>
                    </Card.Body>


                </Card>

            </Container>
        </div>




    )
}