import { Room } from "../../entities/room";
import { Feature } from "../../entities/feature";

export function Summary({features}: Room) {
    return (
        <ul>
            {features.map(f => 
                <li>
                    {f.name}
                </li>
            )}
        </ul>
    )
}