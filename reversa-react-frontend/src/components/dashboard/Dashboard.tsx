import { Student } from "../../entities/Student";
import { Timeline } from "./Timeline";

export function Dashboard(student: Student) {
    
    return (
        <div className="d-flex p-2">
            <Timeline {...student} />
        </div>
    )
}