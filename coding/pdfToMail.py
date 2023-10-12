from pdf_mail import sendpdf

obj = sendpdf(
    "stefenwarner13@gmail.com",
    "ramumeegada18@gmail.com",
    "iyutbwcpmhehhmuc",
    "pdf document",
    "this is a body",
    "kane",
    "/home/apptunix/Pictures/"
)

obj.email_send()
print("done")