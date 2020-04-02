'use strict';

/* eslint prefer-template:off */

const _ = require('lodash');
const chai = require('chai');

const testModule = require('./calculate_to_sum');

const expect = chai.expect;

describe('Testing calculate_to_sum.js', function () {
    context('Testing solution()', function () {
        const tests = {
            1: {
                input: 123456789,
                expectedResult: '1+2+3-4+5+6+78+9\n' +
                    '1+2+34-5+67-8+9\n' +
                    '1+23-4+5+6+78-9\n' +
                    '1+23-4+56+7+8+9\n' +
                    '12+3+4+5-6-7+89\n' +
                    '12+3-4+5+67+8+9\n' +
                    '12-3-4+5-6+7+89\n' +
                    '123+4-5+67-89\n' +
                    '123+45-67+8-9\n' +
                    '123-4-5-6-7+8-9\n' +
                    '123-45-67+89'
            }
        };

        _.map(tests, function (testCase, caseNumber) {
            it(`CASE ${caseNumber}`, function () {
                const result = testModule.solution(testCase.input);

                expect(result).to.be.eql(testCase.expectedResult);
            });
        });
    });
});
