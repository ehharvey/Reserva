import { RoomSize } from "./room-size"

export interface Room {
    id: bigint
    location: string
    name: string
    size: RoomSize
}