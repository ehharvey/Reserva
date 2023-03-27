import { Card } from "react-bootstrap";
import { ScheduleItem } from "../../entities/ScheduleItem";

export function TimelineDayItem(schedule_item: ScheduleItem) {
    return (
        <Card>
            <Card.Header>
                {schedule_item.startDate.toLocaleTimeString()}
            </Card.Header>
            <Card.Img variant="top" src={schedule_item.room.image_url} />
            <Card.Title>
                
            </Card.Title>
            <Card.Body>
                <Card.Text>
                    {schedule_item.endDate.toLocaleTimeString()}
                    {schedule_item.room.name}
                </Card.Text>
            </Card.Body>
        </Card>
    )
}