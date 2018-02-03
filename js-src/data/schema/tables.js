module.exports = {
    accounts: {
        port: { type: 'integer', nullable: false },
        password: { type: 'string', nullable: false },
    },
    flows: {
        port: { type: 'integer', maxlength: 60, nullable: false },
        flow: { type: 'bigInteger' },
        time: { type: 'bigInteger', nullable: false }
    }
};
