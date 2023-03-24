import Table from 'react-bootstrap/Table';
import { Student } from "../../entities/Student"

export function Timeline({schedule}: Student) {
    return (
        <Table striped bordered>
            <thead>
                <tr>
                    <th>
                        Room
                    </th>
                    <th>
                        Time
                    </th>
                </tr>
            </thead>
            <tbody>
                {schedule.items.map(i =>
                    <tr>
                        <td>
                            {i.room.location.name}
                        </td>
                        <td>
                            {i.datetime.toLocaleTimeString()}
                        </td>
                    </tr>)}
            </tbody>
        </Table>
    )
}