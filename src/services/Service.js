import nodemailer from "nodemailer";

class EmailService {
    constructor() {
        this.sendEmail = this.sendEmail.bind(this);
        this.email = "gillem.leonf@gmail.com";
        this.password = "486279315";
        this.transporter = nodemailer.createTransport({
            port: 465,
            host: "smtp.gmail.com",
            auth: {
                user: "gillem.leonf@gmail.com",
                pass: `${this.password}`,
            },
            secure: true,
        });
    }

    sendEmail(req, res) {
        if(!req.body) {
            return res.status(400).json({
                errors: "Request body is empty"
            })
        } else {
            const {name, subject, message, email} = req.body;
            const mailData = {
                from: this.email,
                to: email,
                subject: subject,
                text: "TEXT",
                html: `
                    <div>
                         <p><b>Name:</b> ${name}</p>    
                         <p><b>Subject:</b> ${subject}</p>    
                         <p><b>Email:</b> ${email}</p>    
                         <p><b>Message:</b> ${message}</p>    
                    </div> 
                `
            };
            this.transporter.sendMail(mailData, function (err, info) {
                if(err) {
                    return res.status(500).json({
                        message: "Error sending email",
                        errorCode: 500,
                        error: err
                    })
                } else {
                    return res.status(200).json({
                        message: "Successful"
                    })
                }
            });
        }
    }
}

export default EmailService;