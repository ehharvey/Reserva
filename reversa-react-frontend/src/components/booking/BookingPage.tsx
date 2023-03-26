import { Group } from "../../entities/Group";
import { Button, Card, Container, Form, ListGroup, ListGroupItem } from "react-bootstrap";
import CardHeader from "react-bootstrap/esm/CardHeader";

export function BookingPage({ groups }: { groups: Group[] }) {
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
                                    <Form.Select aria-label="Default select example">
                                        <option>Open this select menu</option>
                                        {groups.map((group) => (
                                            <option key={group.id} value={group.id}>
                                                {group.name}
                                            </option>
                                        ))}
                                        <option value="new">Create new group</option>
                                    </Form.Select>
                                </Form.Group>
                                <Form.Group className="mb-3" controlId="formBasicCheckbox">
                                    <Form.Check type="checkbox" label="Book as group" />

                                    <Form.Check type="checkbox" label="Study With Me" />
                                </Form.Group>
                                <Button variant="primary" type="submit">
                                    Submit
                                </Button>
                            </Form>

                        </Card.Text>
                    </Card.Body>


                </Card>

            </Container>
        </div>




    )
}