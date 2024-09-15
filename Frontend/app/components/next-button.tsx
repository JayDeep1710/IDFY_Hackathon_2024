"use client";

import Link from "next/link";

const NextButton = () => {
  return (
    <Link href={'/select/'} className="items-center flex px-12 h-16 text-3xl border border-[#5EF6FF] glow-on-hover">
      NEXT
    </Link>
  );
};
export default NextButton;
