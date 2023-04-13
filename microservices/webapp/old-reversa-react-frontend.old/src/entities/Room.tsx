import { Feature } from "./Feature"
import { Location } from "./Location"
import { RoomSize } from "./RoomSize"

export interface Room {
    id: number
    location: Location
    name: string
    size: RoomSize
    image_url: string
    features: Array<Feature>
    
}