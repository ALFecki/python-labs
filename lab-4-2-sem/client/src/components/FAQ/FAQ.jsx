import React from 'react';
import styles from './FAQ.module.css';

const FAQ = () => {
    return (
        <div>
            <h1 className={styles.title}>FAQ</h1>

            <div className={styles.detailscontainer}>
                <summary className={styles.summary} type="button" aria-expanded="true">
                    What are your shipping options and rates?
                </summary>
                <p className={styles.content}>
                    We offer various <strong>shipping options</strong>, including standard, express, and international shipping.
                    Shipping rates are calculated based on the <em>weight and destination of the package</em>. You can find detailed
                    information about our shipping options and rates during the checkout process.
                </p>
            </div>

            <div className={styles.detailscontainer}>
                <summary className={styles.summary} type="button" aria-expanded="true">
                    Can I track my order?
                </summary>
                <p className={styles.content}>
                    <strong>Yes</strong>, once your order is shipped, you will receive a tracking number via email. You can use this
                    tracking number to monitor the status and location of your package.
                </p>
            </div>

            <div className={styles.detailscontainer}>
                <summary className={styles.summary} type="button" aria-expanded="true">
                    What is your return policy?
                </summary>
                <p className={styles.content}>
                    <strong>We</strong> accept returns within 30 days of purchase. The item must be unused, in its original packaging,
                    and accompanied by the receipt or proof of purchase. Please refer to our Returns and Refunds policy page for more
                    information and instructions on how to initiate a return.
                </p>
            </div>

            <div className={styles.detailscontainer}>
                <summary className={styles.summary} type="button" aria-expanded="true">
                    How can I contact your customer support team?
                </summary>
                <p className={styles.content}>
                    You can reach our customer support team by emailing <code>support@toy-store.com</code> or by calling our toll-free
                    number <em>(XXX-XXXX-XXXX)</em>. Our team is available [mention the hours of operation]to assist you with any inquiries or concerns you may have.
                </p>
            </div>
        </div>
    );
};

export default FAQ;