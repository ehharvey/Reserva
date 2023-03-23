import { REPL_MODE_SLOPPY } from "repl";
import { Room } from "../../entities/room";
import { Calendar } from "./Calendar";
import { HeadShot } from "./HeadShot";
import { Summary } from "./Summary";
import Title from "./Title";

export function Details(room : Room ) {

    return (
        <div>
            <div>
                <Title {...room}/>
            </div>
            <div>
                <HeadShot {...room} />
                <Summary {...room} />
                <Calendar />
            </div>
        </div>
    )
}