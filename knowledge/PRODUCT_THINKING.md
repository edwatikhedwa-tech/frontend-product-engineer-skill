# Product Thinking

Before planning or UI implementation, establish the project context:

- product and primary users;
- primary jobs, decisions, and critical flows;
- existing design language, tokens, and component system;
- business, technical, accessibility, and compatibility constraints;
- protected areas and behavior that must not change;
- technical stack, installed versions, and project commands;
- project-specific acceptance criteria and required evidence.

Then answer:

1. Who is the primary user and what context are they in?
2. What job are they trying to complete?
3. What decision or action should become easier?
4. What is the smallest useful happy path?
5. What are the important failure, empty, permission, and recovery states?
6. What information is stable, optional, urgent, or destructive?
7. What business or technical constraints are non-negotiable?

Translate the answers into a short screen brief: user, job, inputs, outputs, primary action, secondary actions, states, content risks, and success evidence. If an answer is unknown, mark it as an assumption and ask only when it changes architecture, safety, compatibility, cost, or business logic.

Do not begin CREATE mode by generating a random collection of cards. Establish the workflow, information architecture, and hierarchy first.
