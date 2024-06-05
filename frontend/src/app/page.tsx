import Image from "next/image";

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
      </div>
    </main >
  );
}
