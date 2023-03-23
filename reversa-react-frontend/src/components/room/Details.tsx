import { Room } from "../../entities/Room";
import { Card, ListGroup, Image, Button, Badge } from 'react-bootstrap';

export function Details(room: Room) {

    return (
        <Card style={{ width: '30em' }}>
            <Card.Title>{room.name}</Card.Title>
            <Card.Subtitle>{room.location.name}</Card.Subtitle>
            <Card.Img  variant="top" src={room.image_url} />
            <Card.Body>
                <ListGroup variant="flush">
                    {room.features.map(f =>
                        <ListGroup.Item className="d-flex justify-content-between align-items-start">
                            <Image style={{ height: "auto", width: "3em" }} thumbnail={true} src={f.icon_path} />
                            {f.name}
                            <Badge bg="primary">{f.quantity}</Badge>
                        </ListGroup.Item>
                    )}
                </ListGroup>
            </Card.Body>
            <Card.Footer>
                <Button>Book Room</Button>
            </Card.Footer>
        </Card>
    )
}