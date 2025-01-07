"use client";

import type React from "react";
import { useState } from "react";
import examples from "./examples";
import { useStream } from "@/app/_hooks/useStream";
import {
  generateGuide,
} from "@/app/actions/streamable_objects";
import { Content } from "./Shared";

export const dynamic = "force-dynamic";
export const maxDuration = 60;

const Home: React.FC = () => {
  const [query, setQuery] = useState<string>(examples[0].query);
  const recipie = useStream(generateGuide);

  return (
    <Content
      query={query}
      setQuery={setQuery}
      answer={recipie}
    />
  );
};

export default Home;
