-- upgrade --
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" TEXT NOT NULL UNIQUE,
    "password" VARCHAR(100),
    "email" TEXT  UNIQUE,
    "created_on" DATE NOT NULL,
    "updated_on" DATE,
    "force_password_reset" BOOL,
    "is_login" BOOL
);
CREATE TABLE IF NOT EXISTS "questions" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "question_text" TEXT NOT NULL,
    "description" TEXT,
    "answered" BOOL NOT NULL  DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "answers" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "votes" BIGINT NOT NULL,
    "answer_text" TEXT NOT NULL,
    "accepted" BOOL NOT NULL  DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "question_id" BIGINT NOT NULL REFERENCES "questions" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "comments" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "entity_type" SMALLINT NOT NULL,
    "comment_text" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "answer_id" BIGINT NOT NULL REFERENCES "answers" ("id") ON DELETE CASCADE,
    "answer_entity_id" BIGINT NOT NULL REFERENCES "answers" ("id") ON DELETE CASCADE,
    "question_entity_id" BIGINT NOT NULL REFERENCES "questions" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "comments"."entity_type" IS 'entity_type';
CREATE TABLE IF NOT EXISTS "ratings" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "rating_star" BIGINT NOT NULL,
    "answer_id" BIGINT NOT NULL REFERENCES "answers" ("id") ON DELETE CASCADE,
    "question_id" BIGINT NOT NULL REFERENCES "questions" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
