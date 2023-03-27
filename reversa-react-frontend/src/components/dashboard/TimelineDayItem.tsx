import { Card } from "react-bootstrap";
import { ScheduleItem } from "../../entities/ScheduleItem";

function getTimeUntilFutureDate(futureDate: Date): string {
    const now = new Date();
    const timeDifferenceMs = futureDate.getTime() - now.getTime();

    if (timeDifferenceMs <= 0) {
        return 'Date has already passed!';
    }

    const seconds = Math.floor(timeDifferenceMs / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);
    const months = Math.floor(days / 30);
    const years = Math.floor(months / 12);

    if (years > 0) {
        return `${years} year${years > 1 ? 's' : ''} from now`;
    }

    if (months > 0) {
        return `${months} month${months > 1 ? 's' : ''} from now`;
    }

    if (days > 0) {
        return `${days} day${days > 1 ? 's' : ''} from now`;
    }

    if (hours > 0) {
        return `${hours} hour${hours > 1 ? 's' : ''} from now`;
    }

    if (minutes > 0) {
        return `${minutes} minute${minutes > 1 ? 's' : ''} from now`;
    }

    return `${seconds} second${seconds > 1 ? 's' : ''} from now`;
}

function getTimeRange(startDate: Date, endDate: Date): string {
    const startYear = startDate.getFullYear();
    const endYear = endDate.getFullYear();
    const startMonth = startDate.toLocaleString('default', { month: 'short' });
    const endMonth = endDate.toLocaleString('default', { month: 'short' });
    const startDay = startDate.getDate();
    const endDay = endDate.getDate();
    const startHour = startDate.getHours() % 12 || 12;
    const endHour = endDate.getHours() % 12 || 12;
    const startPeriod = startDate.getHours() >= 12 ? 'PM' : 'AM';
    const endPeriod = endDate.getHours() >= 12 ? 'PM' : 'AM';
    const startMinute = startDate.getMinutes().toString().padStart(2, '0');
    const endMinute = endDate.getMinutes().toString().padStart(2, '0');

    if (startYear === endYear) {
        if (startDate.getMonth() === endDate.getMonth()) {
            if (startDate.getDate() === endDate.getDate()) {
                if (startHour === endHour) {
                    if (startMinute === endMinute) {
                        return `At ${startHour}:${startMinute} ${startPeriod}`;
                    } else {
                        return `From ${startHour}:${startMinute} ${startPeriod} to ${endMinute} minutes past ${endHour} ${endPeriod}`;
                    }
                } else {
                    return `From ${startHour}:${startMinute} ${startPeriod} to ${endHour}:${endMinute} ${endPeriod}`;
                }
            } else {
                return `From ${startMonth} ${startDay} to ${endDay}`;
            }
        } else {
            return `From ${startMonth} ${startDay} to ${endMonth} ${endDay}`;
        }
    } else {
        return `From ${startMonth} ${startDay}, ${startYear} to ${endMonth} ${endDay}, ${endYear}`;
    }
}


export function TimelineDayItem(schedule_item: ScheduleItem) {
    return (
        <Card>
            <Card.Header>
                {getTimeUntilFutureDate(schedule_item.startDate)}
            </Card.Header>
            <Card.Img variant="top" src={schedule_item.room.image_url} />
            <Card.Title>
                {schedule_item.room.name}
            </Card.Title>
            <Card.Subtitle>
                {schedule_item.room.location.name}
            </Card.Subtitle>
            <Card.Footer>
                {getTimeRange(schedule_item.startDate, schedule_item.endDate)}
            </Card.Footer>
        </Card>
    )
}