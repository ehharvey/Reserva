import { Student } from "../../entities/Student";
import { CreditSummary } from "./CreditSummary";
import { Timeline } from "./Timeline";

export function Dashboard(student: Student) {
    
    return (
        <div className="d-flex align-items-start flex-wrap" style={{ gap:"20px" }}>
            <Timeline {...student} />
            <CreditSummary {...student} />            
        </div>
    )
}