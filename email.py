def notify_on_comment(issue_id, comment):
    subscribers = get_issue_subscribers(issue_id)

    for user in subscribers:
        send_email(
            to=user.email,
            subject="New comment added",
            body=comment.text
        )
