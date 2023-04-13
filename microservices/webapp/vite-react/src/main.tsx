import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { MantineProvider } from '@mantine/core'
import { AppHeader } from './components/header/AppHeader'
import './index.css'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <MantineProvider>
      <AppHeader />
      <App />
    </MantineProvider>
  </React.StrictMode>,
)
