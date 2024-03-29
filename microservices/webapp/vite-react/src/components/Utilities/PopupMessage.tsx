import { ActionIcon, Card, CloseButton, Group, Text } from "@mantine/core";
import { IconCalendarEvent, IconMoodSad } from "@tabler/icons-react";
import { useState } from "react";

export interface PopupMessageProps {
    iconType: 'error' | 'calendarEvent'; // define the prop for icon type
    message: string;
    size: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
    w?: number;
    onClose: () => void;
}

export function PopupMessage(props: PopupMessageProps) {
    const { iconType, message, size, w, onClose } = props;

    const getIcon = () => {
        if (iconType === 'error') {
            return <IconMoodSad size="xs" color="red" />;
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