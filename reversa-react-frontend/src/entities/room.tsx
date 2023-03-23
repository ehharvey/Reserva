import { Url } from "url"
import { Feature } from "./feature"
import { RoomSize } from "./room-size"

export interface Room {
    id: bigint
    location: string
    name: string
    size: RoomSize
    image_url: string
    features: Array<Feature>
}