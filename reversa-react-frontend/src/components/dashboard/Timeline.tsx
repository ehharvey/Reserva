import { Card, Container, Stack } from 'react-bootstrap';
import { ScheduleItem } from '../../entities/ScheduleItem';
import { Student } from "../../entities/Student"
import { TimelineDay } from './TimelineDay';
import { TimelineDayItem } from './TimelineDayItem';


function groupScheduleItemsByDay(items: ScheduleItem[]): ScheduleItem[][] {
    const groups = new Map<string, ScheduleItem[]>();

    for (const item of items) {
        const key = item.startDate.toISOString().substr(0, 10);
        if (groups.has(key)) {
            groups.get(key)!.push(item);
        } else {
            groups.set(key, [item]);
        }
    }

    const sortedGroups = Array.from(groups.values()).map((group) =>
        group.sort((a, b) => a.startDate.getTime() - b.startDate.getTime())
    );

    return sortedGroups;
}



export function Timeline({ schedule }: Student) {
    var schedule_by_day = groupScheduleItemsByDay(schedule.items);

    return (
        <Container style={{ maxWidth: "720px" }}>
            <h1 className='text-center'>Upcoming</h1>
            <Stack direction="vertical" gap={5}>
                {schedule_by_day.map((items, index) => (
                    <TimelineDay key={index} date={items[0].startDate}>
                        {items.map((item, index) => (
                            <TimelineDayItem key={index} {...item} />
                        ))}
                    </TimelineDay>
                ))}
            </Stack>
        </Container>
    )
}