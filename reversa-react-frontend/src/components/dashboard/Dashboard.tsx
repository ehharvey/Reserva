import Stack from "react-bootstrap/Stack";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Student } from "../../entities/Student";
import { Timeline } from "./Timeline";

export function Dashboard(student: Student) {
    
    return (
        <Container>
            <Row>
                <Col>
                    
                </Col>
                <Col>
                    <Timeline />
                </Col>
            </Row>
        </Container>
    )
}