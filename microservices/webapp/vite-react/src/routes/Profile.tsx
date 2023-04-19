import { Avatar, Center } from "@mantine/core"

export function Profile() {

  return (
    <div>
      <h1>My Profile</h1>
      <Center inline>
        <Avatar radius="xl" size="xl"/>
      </Center>
    </div>
  )
}