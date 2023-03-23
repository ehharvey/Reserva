import { Room } from "../../entities/room";

export default function Title({name}: Room) {
    return(
        <div>
            <h1>{name}</h1>
        </div>
    )
}