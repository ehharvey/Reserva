import { Container, Stack } from "react-bootstrap";
import { ScheduleItem } from "../../entities/ScheduleItem";
import { TimelineDayItem } from "./TimelineDayItem";

type TimelineDayProps = {
    children: any
    date: Date
}

export function TimelineDay({ date, children }: TimelineDayProps) {
    return (
        <Container>
            <h2>{date.toLocaleDateString()}</h2>
            <Stack direction="horizontal" gap={3}>
                {children}
            </Stack>
        </Container>
    )
}