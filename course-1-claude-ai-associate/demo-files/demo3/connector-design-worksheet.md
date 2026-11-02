# Connector Design Worksheet: Pinecrest Service Desk

Connector name: Pinecrest Service Desk
Purpose in one sentence: Let staff ask Claude about member service requests and fees without opening three systems.

## Part 1: Decide what to expose

Open `tool-catalog.csv`. For each of the ten tools, decide: **Expose now**, **Later phase** or **Never**. Write one reason.

| Tool | Decision | Reason |
|------|----------|--------|
| get_member_summary | | |
| search_service_tickets | | |
| get_fee_schedule | | |
| get_full_member_record | | |
| update_member_address | | |
| create_service_ticket | | |
| send_member_email | | |
| run_sql_query | | |
| list_branch_hours | | |
| close_account | | |

## Part 2: Rename the tools Claude would confuse

Claude chooses a tool from its name and description. Rewrite each name and add a one-sentence description that says what it does and when to use it.

| Current name | Better name | Description |
|--------------|-------------|-------------|
| query1 | | |
| get_data | | |
| doStuff | | |

## Part 3: Authentication and reach

- How does each staff member connect: with their own sign-in, or a shared account?
- What can a staff member reach after connecting?
- What is the first thing a security reviewer will ask about?

## Part 4: Approval path

Number these in the order they should happen, then name an owner for each:

- Pilot group uses it for two weeks
- Request submitted with the tool list
- Published to all staff
- Security review of tools and data returned
