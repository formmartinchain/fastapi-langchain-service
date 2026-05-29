# Prompts

The default chat prompt is built in `chains/chat.py`.

It contains:

- a configurable system prompt from `CHAIN_SYSTEM_PROMPT`
- a user message
- optional session and metadata context

Keep prompt changes close to the chain builder so they can be reviewed alongside
provider settings and output parsing.
