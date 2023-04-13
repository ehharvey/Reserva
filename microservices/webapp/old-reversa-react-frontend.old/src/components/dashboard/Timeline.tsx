import { Card, Container, Stack } from 'react-bootstrap';
import { ScheduleItem } from '../../entities/ScheduleItem';
import { Student } from "../../entities/Student"
import { TimelineDay } from './TimelineDay';
import { TimelineDayItem } from './TimelineDayItem';


function groupScheduleItemsByDay(scheduleItems: ScheduleItem[]): ScheduleItem[][] {
    // Create an object to store the ScheduleItem arrays by day
    const scheduleItemsByDay: { [day: string]: ScheduleItem[] } = {};
  
    // Iterate over each ScheduleItem object
    scheduleItems.forEach((item) => {
      // Get the day of the ScheduleItem start date as a string in YYYY-MM-DD format
      const day = item.startDate.toISOString();
  
      // If an array for this day doesn't exist yet, create one
      if (!scheduleItemsByDay[day]) {
        scheduleItemsByDay[day] = [];
      }
  
      // Add the ScheduleItem object to the array for this day
      scheduleItemsByDay[day].push(item);
    });
  
    // Convert the object of ScheduleItem arrays by day to an array of arrays
    const scheduleItemsArrays = Object.values(scheduleItemsByDay);
  
    // Sort the arrays by the start date of the first ScheduleItem in each array
    scheduleItemsArrays.sort((a, b) => a[0].startDate.getTime() - b[0].startDate.getTime());
  
    return scheduleItemsArrays;
  }
  


export function Timeline({ schedule }: Student) {
    var schedule_by_day = groupScheduleItemsByDay(schedule.items);

    return (
        <>
        
            <h1 className='text-center'>Upcoming</h1>
            <Stack direction="vertical" gap={5} style={{ display: 'flex', flexWrap: 'wrap' }}>
                {schedule_by_day.map((items, index) => (
                    <TimelineDay key={index} date={items[0].startDate}>
                        {items.map((item, index) => (
                            <TimelineDayItem key={index} {...item} />
                        ))}
                    </TimelineDay>
                ))}
            </Stack>
        </>
    )
}