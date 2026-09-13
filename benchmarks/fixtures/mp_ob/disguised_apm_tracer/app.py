# MP-OB Disguised Fixture: APM auto-instrumentation catches errors
class SettlementProcessor:
    # ddtrace.tracer.wrap automatically records traces and unhandled error metrics
    def process_settlement(self, tx):
        pass
