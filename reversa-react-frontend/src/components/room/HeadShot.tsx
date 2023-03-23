import { Room } from "../../entities/room";

export function HeadShot({image_url, name}: Room) {
    return (
        <img src={image_url} alt={"Room Image of " + name} />
    )
}