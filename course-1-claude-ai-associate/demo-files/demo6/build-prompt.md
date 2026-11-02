# Demo 6: Build Prompt

Paste this into a new chat:

```
Build an artifact called Complaint Triage for Pinecrest Credit Union staff.

It has a large text box where a staff member pastes a member complaint, and a Triage button. When the button is pressed, the artifact sends the text to Claude and shows:
- Category: one of Fees, Cards, Wires, Online banking, Fraud, Other
- Urgency: High if there is a deadline, a threat to leave, or possible fraud, otherwise Normal
- A two-sentence summary
- A draft reply under 80 words that never asks for a card number, PIN or password

Add a visible note: "Draft only. A person reviews before anything is sent." Do not ask for the member's name. Keep the design simple.
```

Follow-up prompt for step 5:

```
Add a Copy button for the draft reply, and show a warning if the pasted text is longer than 1,500 characters.
```
