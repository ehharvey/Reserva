import { ActionIcon, Button, Container, Grid, Group, SimpleGrid, Stack } from "@mantine/core";
import { WheelEventHandler, useEffect, useState } from "react";
import { TimeRange } from "../../routes/BookingForm";


const hoursPerDay = 24;
const blockDuration = 30; // minutes, <= 60, and only use number that divides 60 evenly
const blocksPerHour = 60 / blockDuration;
const buttonHeight = 30;
const displayRows = 5;
const displayCols = 2;
const ColumnWidth = 120;
const GridWidth = ColumnWidth * displayCols;
const gridSpacing = 5;


export interface TimeBlocksProps {
    onChange: (timeRange: TimeRange) => void;
    // onTimeBlockDeselect: () => void;
    w?: number | string;
}

type TimeBlock = {
    startTime: string,
    available: boolean,
}

export var ResetTimeBlocks: () => void;

export function TimeBlocks(props: TimeBlocksProps) {
    const { w } = props;

    const [selectedStartTime, setSelectedStartTime] = useState<number | null>(null);
    const [selectedEndTime, setSelectedEndTime] = useState<number | null>(null);

    //Update time range in the input field when start time or end time is changed
    useEffect(() => {
        if (selectedStartTime !== null && selectedEndTime !== null) {
          const startTime = new Date(timeBlocks[selectedStartTime].startTime);
          const endTime = new Date(timeBlocks[selectedEndTime].startTime);        
          props.onChange({ startTime: startTime, endTime: endTime });
        }
        else if(selectedStartTime !== null) {
            const startTime = new Date(timeBlocks[selectedStartTime].startTime);
            props.onChange({ startTime: startTime });
        }
        else {
          props.onChange({});
        }
      }, [selectedStartTime, selectedEndTime]);

      ResetTimeBlocks = () => {
        setSelectedStartTime(null);
        setSelectedEndTime(null);
    }

    //Time blocks for a day
    const timeBlocks: TimeBlock[] = [];

    const startTime = new Date();
    startTime.setHours(0, 0, 0, 0); // Set start time to midnight
    const endTime = new Date();
    endTime.setHours(23, 59, 59, 999); // Set end time to 11:59 PM of the same day

    //Create all time blocks for a day
    let currentTime = startTime;

    while (currentTime < endTime) {
        const startTime = new Date(currentTime);
        const endTime = new Date(
            currentTime.getTime() + blockDuration * 60000
        );

        timeBlocks.push({
            startTime: startTime.toISOString(),
            available: true,
        });

        currentTime = endTime;
    }

    //Fetch unavailable times from server

    return (
        <div >
            <Stack spacing="xs" align="center" mt={10} w={w} sx={{minWidth:255}}>
                <Group>
                    <ActionIcon>

                    </ActionIcon>
                </Group>
                <SimpleGrid style={{ height: buttonHeight * displayRows + gridSpacing * (displayRows - 1), overflow: 'auto' }} w={GridWidth} cols={displayCols} spacing={gridSpacing} verticalSpacing={gridSpacing}>

                    {timeBlocks.map((timeBlock, index) => {
                        const selectedBlockIndex = index;
                        return (

                            <Button key={index} h={buttonHeight}
                                variant={
                                    selectedStartTime === selectedBlockIndex || (selectedStartTime !== null && selectedEndTime !== null && selectedBlockIndex >= selectedStartTime && selectedBlockIndex <= selectedEndTime) ? "filled" : "outline"
                                }
                                onClick={() => {
                                    //if no time block is yet selected, make this the start time
                                    if (selectedStartTime === null) {                       
                                        setSelectedStartTime(selectedBlockIndex);
                                    }
                                    //if a start time is selected, then depend on the selected time block: 
                                    else if (selectedEndTime === null) {
                                        //if selected time block is the same as the start time, then deselect the time block
                                        if (selectedBlockIndex === selectedStartTime) {     
                                            setSelectedStartTime(null);
                                        }
                                        //if selected time block is before the start time, then make the start time become end time and selected time block become start time
                                        else if (selectedBlockIndex < selectedStartTime) {  
                                            setSelectedEndTime(selectedStartTime);
                                            setSelectedStartTime(selectedBlockIndex);
                                        }
                                        //if selected time block is after the start time, then make the selected time block become end time  
                                        else{
                                            setSelectedEndTime(selectedBlockIndex);
                                        }

                                        //if both start and end time is set, set time range
                                        if(selectedStartTime !== null && selectedEndTime !== null){
                                            const startTime = new Date(timeBlocks[selectedStartTime].startTime);
                                            const endTime = new Date(timeBlocks[selectedEndTime].startTime);
                                        }
                                    }
                                    //if both start time and end time are already selected, then make the selected time block become start time and deselect end time
                                    else {
                                        setSelectedStartTime(selectedBlockIndex);
                                        setSelectedEndTime(null);
                                    }
                                }}
                            >
                                <span>{new Date(timeBlock.startTime).toLocaleString([], { hour: 'numeric', minute: '2-digit', hour12: true })}</span>
                            </Button>
                        )
                    })}
                </SimpleGrid>
            </Stack>


            <style>
                {`
                ::-webkit-scrollbar {
                    width: 10px;
                    height: 10px;
                }
                ::-webkit-scrollbar-track {
                    background: #f1f1f1;
                    border-radius: 5px;
                }
                ::-webkit-scrollbar-thumb {
                    background: #888;
                    border-radius: 5px;
                }
            `}
            </style>
        </div>
    )
}