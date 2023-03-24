import { Student } from "../../entities/Student";
import { Timeline } from "./Timeline";

export function Dashboard(student: Student) {
    
    return (
        <div >
            <Timeline {...student} />           
        </div>
    )
}