"use client";
import Image from "next/image";
import GitHubButton from 'react-github-btn';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl flex items-center justify-center font-mono text-sm lg:flex">
        <Image src="/clueso.png" width={400} height={300} alt="logo" />
      </div>
      <div style={{ fontFamily: 'Berkeley, sans-serif' }}>
        <h1 className="text-5xl font-bold">Welcome to Clueso</h1>
        <p>
          Clueso is a simple tool to help busy developers (and investors) stay on top of the latest trending repos on Github.
        </p>
        <div className="my-4">

        </div>
        <div>
          <figure>
            <Image src="/top-repos.png" width={500} height={300} alt="top repos" />
            <figcaption>Top Trending Repositories on GitHub</figcaption>
          </figure>
        </div>
        <div>
          <figure>
            <Image src="/reachouts.png" width={500} height={300} alt="reachouts" />
            <figcaption>Reachouts</figcaption>
          </figure>
        </div>
        <GitHubButton href="https://github.com/arach/clueso.xyz" data-icon="octicon-star" data-size="large" data-show-count="true">
          Find us on GitHub
        </GitHubButton>

      </div>
    </main >
  );
}
