import { useAuth0 } from '@auth0/auth0-react';
import {
    Avatar
  } from '@mantine/core';

export function AvatarProfile() {
  const { user, isAuthenticated } = useAuth0();
  return (
    <>
      {isAuthenticated && user?.picture && (
        <Avatar radius="xl" src={user.picture}/>
      )}
    </>
  );
}