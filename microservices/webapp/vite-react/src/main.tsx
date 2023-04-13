import React from 'react'
import ReactDOM from 'react-dom/client'
import { MantineProvider } from '@mantine/core'
import { AppHeader } from './components/header/AppHeader'

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import { Root } from './routes/Root'
import { Profile } from './routes/Profile';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
  },
  {
    path: "/me",
    element: <Profile />
  }
]);

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <MantineProvider>
      <AppHeader />
      <RouterProvider router={router} />
    </MantineProvider>
  </React.StrictMode>,
)
