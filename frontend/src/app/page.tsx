/**
 * v0 by Vercel.
 * @see https://v0.dev/t/Pvc4wsLY38b
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import Link from "next/link"
import Image from "next/image"

export default function Component() {
  return (
    <div className="flex flex-col min-h-[100dvh] bg-gradient-to-br from-[#1E293B] to-[#4338CA]">
      <header className="px-6 lg:px-12 h-14 flex items-center">
        <Link href="#" className="flex items-center justify-center" prefetch={false}>
          <Image src="/clueso-transparent.png" width={50} height={30} alt="logo" />
          <span className="sr-only">Clueso.xyz</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link
            href="/about"
            className="text-sm font-medium text-white hover:underline underline-offset-4 font-mono"
            prefetch={false}
          >
            About
          </Link>
          <Link
            href="/features"
            className="text-sm font-medium text-white hover:underline underline-offset-4 font-mono"
            prefetch={false}
          >
            Features
          </Link>
          <Link
            href="/technologies"
            className="text-sm font-medium text-white hover:underline underline-offset-4 font-mono"
            prefetch={false}
          >
            Technologies
          </Link>
          <Link
            href="https://github.com/arach/clueso.xyz"
            className="text-sm font-medium text-white hover:underline underline-offset-4 font-mono"
            prefetch={false}
          >
            GitHub
          </Link>
        </nav>
      </header>
      <main className="flex-1">
        <section className="w-full pt-12 md:pt-24 lg:pt-32 border-y border-white/20">
          <div className="px-4 md:px-6 space-y-10 xl:space-y-16">
            <div className="grid max-w-[1300px] mx-auto gap-4 px-4 sm:px-6 md:px-10 md:gap-16">
              <div>
                <h1 className="lg:leading-tighter text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl xl:text-[3.4rem] 2xl:text-[3.75rem] text-white font-['Roboto_Mono', 'monospace']">
                  Clueso.xyz
                </h1>
                <p className="max-w-[900px] text-white/80 md:text-xl font-['Fira_Code', 'monospace']">
                  A simple tool to help busy developers (and investors) stay on top of the latest trending repos on GitHub.
                </p>
                <div className="space-x-4 mt-6">
                  <Link
                    href="https://github.com/arach/clueso.xyz"
                    className="inline-flex h-9 items-center justify-center rounded-md bg-white px-4 py-2 text-sm font-medium text-gray-900 shadow transition-colors hover:bg-gray-100 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 font-['Fira_Code', 'monospace']"
                    prefetch={false}
                  >
                    View on GitHub
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-white font-['Roboto_Mono', 'monospace']">
                  Features
                </h2>
                <p className="max-w-[900px] text-white/80 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed font-['Fira_Code', 'monospace']">
                  Take a look at the key features of the hackathon project.
                </p>
              </div>
            </div>
            <div className="mx-auto grid items-start gap-8 sm:max-w-4xl sm:grid-cols-2 md:gap-12 lg:max-w-5xl lg:grid-cols-2">
              <img
                src="/top-repos.png"
                width="550"
                height="310"
                alt="Top Repos Research Report"
                className="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full"
              />
              <img
                src="/reachouts.png"
                width="550"
                height="310"
                alt="Reachouts"
                className="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full"
              />
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gradient-to-br from-[#4338CA] to-[#6366F1]">
          <div className="container grid items-center justify-center gap-4 px-4 text-center md:px-6 lg:gap-10">
            <div className="space-y-3">
              <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl text-white font-['Roboto_Mono', 'monospace']">
                Technologies Used
              </h2>
              <p className="mx-auto max-w-[700px] text-white/80 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed font-['Fira_Code', 'monospace']">
                The hackathon project was built using the following technologies:
              </p>
            </div>
            <div className="divide-y rounded-lg border border-white/20">
              <div className="grid w-full grid-cols-3 items-stretch justify-center divide-x md:grid-cols-5">
                <div className="mx-auto flex w-full items-center justify-center p-4 sm:p-8">
                  <img
                    src="/crewai.png"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center"
                  />
                </div>
                <div className="mx-auto flex w-full items-center justify-center p-4 sm:p-8">
                  <img
                    src="/perplexity.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center"
                  />
                </div>
                <div className="mx-auto flex w-full items-center justify-center p-8">
                  <img
                    src="/playwright.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center"
                  />
                </div>
                <div className="mx-auto flex w-full items-center justify-center p-4 sm:p-8">
                  <img
                    src="/LangChain-logo.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center"
                  />
                </div>
                <div className="mx-auto flex w-full items-center justify-center p-4 sm:p-8">
                  <img
                    src="/python.png"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center"
                  />
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t border-white/20">
        <p className="text-xs text-white/80 font-['Fira_Code', 'monospace']">
          &copy; 2024 Clueso. All rights reserved.
        </p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link
            href="#"
            className="text-xs text-white hover:underline underline-offset-4 font-['Fira_Code', 'monospace']"
            prefetch={false}
          >
            Terms of Service
          </Link>
          <Link
            href="#"
            className="text-xs text-white hover:underline underline-offset-4 font-['Fira_Code', 'monospace']"
            prefetch={false}
          >
            Privacy
          </Link>
        </nav>
      </footer>
    </div>
  )
}
