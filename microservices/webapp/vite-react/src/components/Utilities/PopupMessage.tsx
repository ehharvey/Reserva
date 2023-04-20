import { ActionIcon, Card, CloseButton, Group, Text } from "@mantine/core";
import { IconCalendarEvent, IconClock } from "@tabler/icons-react";
import { useState } from "react";

export interface PopupMessageProps {
    iconType: 'clock' | 'calendarEvent'; // define the prop for icon type
    message: string;
    size: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
    w?: number;
    onClose: () => void;
}

export function PopupMessage(props: PopupMessageProps) {
    const { iconType, message, size, w, onClose } = props;

    const getIcon = () => {
        if (iconType === 'clock') {
            return <IconClock size="xs" color="grey" />;
        }
        if (iconType === 'calendarEvent') {
            return <IconCalendarEvent size="xs" color="grey" />
        }
        return null;
    };

    const handleOnClose = () => {
        console.log('handleOnClose');
        onClose(); // call the onClose function to inform the parent
    };

    return  (
        <Card withBorder padding="xs">
            <Group position="apart" align="left">
                <Group>
                    <ActionIcon variant="transparent" size={size} disabled>{getIcon()}</ActionIcon>
                    <Text size="xs" align="left">{message}</Text>
                </Group>
                <CloseButton size={size} variant="filled" color="red" onClick={handleOnClose} />
            </Group>
        </Card>
    )
}