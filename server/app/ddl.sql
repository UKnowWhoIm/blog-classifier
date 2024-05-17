

CREATE TABLE IF NOT EXISTS posts(
  id uuid NOT NULL DEFAULT uuid_generate_v4() PRIMARY KEY,
  headline VARCHAR(100) NOT NULL,
  body text NOT NULL,
  category VARCHAR(30)
)

CREATE TABLE IF NOT EXISTS model_responses(
  id uuid NOT NULL DEFAULT uuid_generate_v4() PRIMARY KEY,
  error smallint,
  model VARCHAR(30) NOT NULL,
  category VARCHAR(30),
  system_prompt text,
  prompt text,
  response text,
  total_duration BIGINT,
  post_id uuid NOT NULL REFERENCES posts("id")
)