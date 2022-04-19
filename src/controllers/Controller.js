import EmailService from "../services/Service"

class EmailController {

    constructor() {
        this.sendEmail = this.sendEmail.bind(this);
        this.emailService = new EmailService();
    }

    sendEmail(req, res) {
        this.emailService.sendEmail(req, res)
    }

}

export default EmailController;