import {
    Avatar
  } from '@mantine/core';

export function AvatarProfile() {
  return (
    <>
      {/* Default placeholder */}
      <Avatar radius="xl" onClick={() => { location.href = "../me"}}/>
    </>
  );
}