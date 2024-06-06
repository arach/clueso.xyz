import { Fraunces } from 'next/font/google'
import { IBM_Plex_Mono } from 'next/font/google'
import './globals.css'
import { ReactNode } from 'react';

const fraunces = Fraunces({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-fraunces',
})
const ibm_plex_mono = IBM_Plex_Mono({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-ibm_plex_mono',
  weight: '400',
})

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  return (
    <html lang="en">
      <body className={`${fraunces.variable} ${ibm_plex_mono.variable}`}>
        {children}
      </body>
    </html>
  )
}