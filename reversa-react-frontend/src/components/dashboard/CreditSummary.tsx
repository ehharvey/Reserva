import { Button } from "react-bootstrap";
import { Student } from "../../entities/Student";

export function CreditSummary({credits}: Student) {
    return (
        <Button>
            Credits: {credits}
        </Button>
    )
}